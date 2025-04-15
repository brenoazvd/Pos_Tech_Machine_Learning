from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", safety_checker=None)

prompt = "a fantasy landscape with mountains and a river, in the style of Studio Ghibli"
image = pipe(prompt).images[0]