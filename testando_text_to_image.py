from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5")

prompt = "A llama on a yatch"
image = pipe(prompt).images[0]