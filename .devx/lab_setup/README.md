# Start the VSS Services

<img src="_static/robots/startup.png" alt="VSS Robot Character" style="float:right; max-width:350px;margin:15px;" />


Before getting started, we will use Docker Compose to start the Blueprint.

To do this, you will need an NVIDIA API Key. If you don't already have one, you can [generate an API Key](https://build.nvidia.com/settings/api-keys). This will begin with `nvapi-.....`.

The setup will be done on the command line. To get started, open a new <button onclick="openNewTerminal();"><i class="fas fa-terminal"></i> terminal</button>.

<!--fold:break -->

## Download Data Files

Let's first make sure we have downloaded the data files we will need. The following command will download any required files.

```bash
git lfs pull
```

<!--fold:break -->

## Login to the NGC Registry

Log into NVIDIA's NGC Registry. Use this command and enter your API Key when prompted.

```bash
echo $NVIDIA_API_KEY | docker login -u '$oauthtoken' nvcr.io --password-stdin
```

<!--fold:break -->

## Start the Blueprint services

Now, we will start the VSS Blueprint. Note that these commands will take some time to return as they download and stage the necessary models and code.

A few profiles have been made available depending on your hardware.

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

To start the Blueprint in this configuration, use the following command:

```bash
sudo -E docker compose --profile local-deployment-single-gpu up -d
```

Watch the status of the containers and wait for them to become healthy with this command:

```bash
watch sudo -E docker compose --profile local-deployment-single-gpu ps
```

### **Dual GPUs - min 40GB**

|  | Model | Self-hosted | GPU ID |
| --- | --- | --- | --- |
| VLM | nvila-15b | 🟢 yes | 1 |
| Embedding | nvidia/llama-3.2-nv-embedqa-1b-v2 | 🟢 yes | 2 |
| Reranking | nvidia/llama-3.2-nv-rerankqa-1b-v2 | 🟢 yes | 2 |
| LLM | meta/llama-3.1-8b-instruct | 🟢 yes | 2 |


To start the Blueprint in this configuration, use the following command:

```bash
sudo -E docker compose --profile local-deployment-dual-gpu up -d
```

Watch the status of the containers and wait for them to become healthy with this command:

```bash
watch sudo -E docker compose --profile local-deployment-dual-gpu ps
```

### **Quad GPUs - min 80GB**

|  | Model | Self-hosted | GPU ID |
| --- | --- | --- | --- |
| VLM | vila-40b | 🟢 yes | 1 |
| Embedding | nvidia/llama-3.2-nv-embedqa-1b-v2 | 🟢 yes | 2 |
| Reranking | nvidia/llama-3.2-nv-rerankqa-1b-v2 | 🟢 yes | 2 |
| LLM | meta/llama-3.1-70b-instruct | 🟢 yes | 3 |


To start the Blueprint in this configuration, use the following command:

```bash
sudo -E docker compose --profile local-deployment-quad-gpu up -d
```

Watch the status of the containers and wait for them to become healthy with this command:

```bash
watch sudo -E docker compose --profile local-deployment-quad-gpu ps
```

<!-- tabs:end -->

Once all of the services have a status of `Up` and `healthy`, you are ready to continue.
