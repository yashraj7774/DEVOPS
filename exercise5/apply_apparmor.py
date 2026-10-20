import docker

client = docker.from_env()

print("Building image...")
client.images.build(path=".", tag="flask-apparmor")

print("Starting container with AppArmor profile...")

container = client.containers.run(
    "flask-apparmor",
    ports={"5000/tcp": 5001},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

try:
    print("Container started:", container.short_id)

    info = client.api.inspect_container(container.id)
    print("Configured security options:",
          info["HostConfig"]["SecurityOpt"])

finally:
    container.stop()
    container.remove()
    print("Container stopped and removed.")
