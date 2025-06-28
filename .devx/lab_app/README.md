# Video Inspection Agent

<img src="_static/robots/blueprint.png" alt="VSS Robot Character" style="float:right; max-width:350px;margin:15px;" />

After using a Jupyter Notebook to prototype an application, the learnings from that notebook are then converted into an application. In the last exercise, we prototyped our VSS solution.
Now we will use the learnings in <button onclick="openOrCreateFileInJupyterLab('code/Custom_VSS.ipynb');"><i class="fas fa-flask"></i> code/Custom_VSS.ipynb</button> to create a custom Python application.

<!--fold:break -->

## Automated Inspections and Audits

Today, we will be assisting local governments with infrastructure inspections.
Drone pilots will submit inspection footage which will then be triaged by our AI agent.

It is critical that findings from these videos get routed to the correct department.
It is also vital that safety related issues be escalated to the highest priority.

<!--fold:break -->

## Creating your application

<img src="_static/robots/wrench.png" alt="VSS Robot Character" style="float:left; max-width:200px;margin:15px;" />

Open <button onclick="openOrCreateFileInJupyterLab('code/bridge_inspector.py');"><i class="fa-brands fa-python"></i> code/bridge_inspector.py</button> and we can get started by checking out the initial code.

This file already has a handful of functions templated. We will work on filling these in.

At the bottom of the file is a function called `main`. This is the entry point to our application.
This function accepts two arguments, both of which will be defined on the command line at run time.

This function has the following structure:
  - <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# get the first model name');">Read in the first model id</button> 
  - **For each video file:**
    - <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# upload the video');">Upload the video</button> 
    - <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# summarize the video');">Summarize the video</button> 
    - <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# ask follow up questions');">Chat with the video to get more detail</button> 

The remaining functions will be called by the `main` function to accomplish this task.

<!--fold:break -->

## Testing your application

To test this application as we write it, open a new <button onclick="openNewTerminal();"><i class="fas fa-terminal"></i> terminal</button>.

To test your application, open a Terminal in Jupyter and navigate to `code/`.

```bash
cd code
```

Run your application from the command line:

```bash
./bridge_inspector.py ../assets/bridge.mp4
```

For now, you'll see an error. But as we develop our application, you will see more here.

<!--fold:break -->

### Query Model ID

Inside of the `main` function, at <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# get the first model name');"># get the first model name</button>, we need to call the <button onclick="goToLineAndSelect('code/bridge_inspector.py', 'def lookup_model_id');">lookup_model_id</button> function. The function also needs to be populated.

Reference the previous labs to complete this function.

<!--fold:break -->

### Upload the video file

At this point, we will loop over all the video files specified by the user at runtime. We need to call the function
<button onclick="goToLineAndSelect('code/bridge_inspector.py', 'def upload_video_to_vss');">upload_video_to_vss</button>
function in the
<button onclick="goToLineAndSelect('code/bridge_inspector.py', '# upload the video');"># upload the video</button> block of code.

Remember this is done using a `POST` request and uploading the bytes.

<!--fold:break -->

### Video Summarization

<button onclick="goToLineAndSelect('code/bridge_inspector.py', 'def summarize_video');">summarize_video</button> should use the uploaded video ID to request a summary of the video. In the last exercise, we made some effective prompts that will help here.

This function should be invoked by <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# summarize the video');"># summarize the video</button> block of code.

Make sure you enable chat!

<!--fold:break -->

### Chat with your video

Use the `Chat` class from before (it is already imported from `helpers`), and connect to the VSS Chat server. In this example, the VSS URL is provided at runtime. Put this code in the <button onclick="goToLineAndSelect('code/bridge_inspector.py', '# connect to the chat server');"># connect to the chat server</button> block.

<button onclick="goToLineAndSelect('code/bridge_inspector.py', '# ask follow up questions');"># ask follow up questions</button> should use the chat API to request additional information. We need to ask the chat model about maintenance escalations, priority of repairs, a report title, and a list of any emergency repairs that are needed.

We haven't made prompts for this yet, but try it out yourself.

<details>
<summary><b>💢 Stuck?</b></summary>

```python
escalations = chat_client.query("List any necessary escalations for maintenance.")
priority = chat_client.query("Score the priority of this report.")
emergencies = chat_client.query("Does this bridge require immediate structural attention?")
```

</details>

<!--fold:break -->

### Verify the results

At this point, your application should be run in the terminal without errors. When everything works correctly, a Markdown report will be shown. How is the report? You can go back and make changes to your prompts to change what information is documented.

<!--fold:break -->

## 🦾 Congratulations on your new agent

<img src="_static/robots/blueprint-blend.png" alt="VSS Robot Character" style="float:right; max-width:350px;margin:15px;" />

You now have a fully fledged Video Search and Summarization agent from the NVIDIA AI Blueprint. This can be further integrated into your business processes to unlock domain knowledge from video.
