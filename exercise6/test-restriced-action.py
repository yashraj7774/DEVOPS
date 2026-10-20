import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

try:
    print(f"Container started: {container.short_id}")

    tests = [
        ["cat", "/etc/passwd"],
        ["/bin/bash", "-c", "echo BASH_EXECUTED"]
    ]

    for command in tests:
        result = container.exec_run(command)

        print(f"\nCommand: {' '.join(command)}")
        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output.decode(errors='replace')}")

finally:
    container.stop()
    container.remove()
    print("\nContainer stopped and removed.")
