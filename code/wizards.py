import ipywidgets as widgets
from IPython.display import display, Markdown
import math
import black

# Constants
VIDEO_RUNTIME = 3 * 60 

def tune_chunks(body):
    """Create a widget for tuning the chunking params."""
    label_layout = widgets.Layout(width="500px")
    
    # Sliders with variable name labels
    num_frames_per_chunk = widgets.IntSlider(
        value=10, min=1, max=20, step=1,
        description='num_frames_per_chunk',
        continuous_update=True,
        layout=label_layout,
        style={'description_width': 'initial'}
    )
    
    chunk_duration = widgets.IntSlider(
        value=30, min=5, max=90, step=1,
        description='chunk_duration',
        continuous_update=True,
        layout=label_layout,
        style={'description_width': 'initial'}
    )
    
    chunk_overlap_duration = widgets.IntSlider(
        value=0, min=0, max=90, step=1,
        description='chunk_overlap_duration',
        continuous_update=True,
        layout=label_layout,
        style={'description_width': 'initial'}
    )
    
    output = widgets.Output()
    
    def update_display(change=None):
        with output:
            output.clear_output()
            if chunk_duration.value <= chunk_overlap_duration.value:
                display(Markdown("⚠️ **chunk_duration must be greater than chunk_overlap_duration.**"))
                return

            display(Markdown("## Try tuning these parameters"))
            body["num_frames_per_chunk"] = num_frames_per_chunk.value
            body["chunk_duration"] = chunk_duration.value
            body["chunk_overlap_duration"] = chunk_overlap_duration.value
            
            effective_chunk = chunk_duration.value - chunk_overlap_duration.value
            num_chunks = math.ceil(VIDEO_RUNTIME / effective_chunk)
            total_frames = num_chunks * num_frames_per_chunk.value
    
            display(Markdown(f"""
### Results
- `video_runtime`: {VIDEO_RUNTIME} seconds
- `effective_chunk`: {effective_chunk} seconds
- `num_chunks`: {num_chunks}
- `num_frames`: {total_frames}
"""))

            code_str = f"body = { body }"
            formatted_code = black.format_str(code_str, mode=black.Mode())
            display(Markdown(f"""
```python
{ formatted_code }
```
"""))

    for w in [num_frames_per_chunk, chunk_duration, chunk_overlap_duration]:
        w.observe(update_display, names="value")
    
    # Wrap in VBox (vertical layout), then center with HBox
    app = widgets.VBox([
        num_frames_per_chunk,
        chunk_duration,
        chunk_overlap_duration,
        output
    ])

    centered_app = widgets.HBox([app], layout=widgets.Layout(justify_content='center'))

    display(centered_app)
    update_display()

    return (num_frames_per_chunk, chunk_duration, chunk_overlap_duration)
