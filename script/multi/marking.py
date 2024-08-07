from IPython import get_ipython
from pathlib import Path
import json

home = Path.home()
src = home / '.gutris1'
mark = src / 'marking.json'

def del_var():
    variables = ['webui', 'models', 'webui_output', 'extensions', 'embeddings',
                 'vae', 'ckpt', 'tmp_ckpt', 'lora', 'tmp_lora', 'forge_svd']

    for var in variables:
        if var in globals():
            del globals()[var]

def get_name(path):
    with open(path, 'r') as file:
        value = json.load(file)
        return value.get('ui', None)

if mark.exists():
    del_var()
    
    ui = get_name(mark)

    if ui == 'A1111':
        webui = home / 'asd'
        models = webui / 'models'
        webui_output = webui / 'outputs'
        extensions = webui / 'extensions'
        embeddings = webui / 'embeddings'
        vae = models / 'VAE'
        ckpt = models / 'Stable-diffusion'
        tmp_ckpt = models / 'Stable-diffusion/tmp_ckpt'
        lora = models / 'Lora'
        tmp_lora = models / 'Lora/tmp_lora'

    elif ui == 'Forge':
        webui = home / 'forge'
        models = webui / 'models'
        webui_output = webui / 'output'
        extensions = webui / 'extensions'
        embeddings = webui / 'embeddings'
        vae = models / 'VAE'
        ckpt = models / 'Stable-diffusion'
        tmp_ckpt = models / 'Stable-diffusion/tmp_ckpt'
        lora = models / 'Lora'
        tmp_lora = models / 'Lora/tmp_lora'
        forge_svd = models / 'svd'

    elif ui == 'ComfyUI':
        webui = home / 'ComfyUI'
        models = webui / 'models'
        webui_output = webui / 'output'
        extensions = webui / 'custom_nodes'
        embeddings = models / 'embeddings'
        vae = models / 'vae'
        ckpt = models / 'checkpoints'
        tmp_ckpt = models / 'checkpoints/tmp_ckpt'
        lora = models / 'loras'
        tmp_lora = models / 'loras/tmp_lora'

    else:
        pass
