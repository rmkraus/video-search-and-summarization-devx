# Start the VSS Services

<img src="_static/robots/startup.png" alt="VSS Robot Character" style="float:right; max-width:350px;margin:15px;" />


A Docker Compose file has been provided that will start the blueprint services.
All of these steps will be done in the <button onclick="openNewTerminal();"><i class="fas fa-terminal"></i> Terminal</button>.

## Login to the NGC Registry

1. [Generate a new API Key](https://build.nvidia.com/settings/api-keys), if you don't already have one. This will begin with `nvapi-.....`.

1. Log into NVIDIA's NGC Registry. Use this command and enter your API Key when prompted.

    ```bash
    sudo docker login -u '$oauthtoken' nvcr.io
    ```

1. Save your API Key in an environment variable.

    ```bash
    export NGC_API_KEY="nvapi-........"
    ```

<!--fold:break -->

## Start the blueprint services

A few profiles have been made avilable depending on your hardware.

{{#isBrev}}
> **Note:** Looks like you are running in Brev! We recommend using the Dual GPU profile for optimal performance.
{{/isBrev}}

<!-- tabs:start -->

### **Single GPU - min 40GB**

|  | Model | Self-hosted | GPU ID |
| --- | --- | --- | -- |
| VLM | nvila-15b | 🟢 yes | 1 |
| Embedding | nvidia/llama-3.2-nv-embedqa-1b-v2 | 🔴 no | |
| Reranking | nvidia/llama-3.2-nv-rerankqa-1b-v2" | 🔴 no |
| LLM | meta/llama-3.1-70b-instruct | 🔴 no | |

To start the blueprint in this configuration, use the following command:

```bash
sudo docker compose --profile local-deployment-single-gpu up -d
```

Watch the status of the containers and wait for them to become healthy with this command:

```bash
watch sudo docker compose --profile local-deployment-single-gpu ps
```

### **Dual GPUs - min 40GB**

|  | Model | Self-hosted | GPU ID |
| --- | --- | --- | --- |
| VLM | nvila-15b | 🟢 yes | 1 |
| Embedding | nvidia/llama-3.2-nv-embedqa-1b-v2 | 🟢 yes | 2 |
| Reranking | nvidia/llama-3.2-nv-rerankqa-1b-v2 | 🟢 yes | 2 |
| LLM | meta/llama-3.1-8b-instruct | 🟢 yes | 2 |


To start the blueprint in this configuration, use the following command:

```bash
sudo docker compose --profile local-deployment-dual-gpu up -d
```

Watch the status of the containers and wait for them to become healthy with this command:

```bash
watch sudo docker compose --profile local-deployment-dual-gpu ps
```

### **Quad GPUs - min 80GB**

|  | Model | Self-hosted | GPU ID |
| --- | --- | --- | --- |
| VLM | nvila-15b | 🟢 yes | 1 |
| Embedding | nvidia/llama-3.2-nv-embedqa-1b-v2 | 🟢 yes | 2 |
| Reranking | nvidia/llama-3.2-nv-rerankqa-1b-v2 | 🟢 yes | 2 |
| LLM | meta/llama-3.1-70b-instruct | 🟢 yes | 3 |


To start the blueprint in this configuration, use the following command:

```bash
sudo docker compose --profile local-deployment-quad-gpu up -d
```

Watch the status of the containers and wait for them to become healthy with this command:

```bash
watch sudo docker compose --profile local-deployment-quad-gpu ps
```

<!-- tabs:end -->

<!--fold:break -->

## Access the Blueprint Interface

Now you are up and running!

{{#isBrev}}
Check out the blueprint demo interface by navigating to https://frontend0-{{ brevId }}.brevlab.com.
{{/isBrev}}
{{^isBrev}}
Check out the blueprint demo interface by navigating to http://{{ hostname }}:9100.
{{/isBrev}}
