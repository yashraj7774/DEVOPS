# Exercise 8 — Creating a "Hello World" Jenkins Job

## 1. Jenkins Freestyle Job

A Freestyle project named `HelloWorld` was created in Jenkins and connected to the GitHub repository `DEVOPS-ASSIGNMENT`. The job retrieves the repository's `main` branch and runs the `hello-world.sh` script from the `exercise8` directory.

![Jenkins HelloWorld Job Successful](jenkins-job-success.png)

---

## 2. Build Console Output

Build **#3** completed successfully. Jenkins checked out the latest code from GitHub, executed `sh exercise8/hello-world.sh`, and printed `Hello, Jenkins!` in the console.

![Jenkins HelloWorld Successful Console Output](jenkins-consol-output.png)

---

## 3. Result

The Jenkins job successfully demonstrated a basic Continuous Integration workflow:

- Source code was stored in the GitHub repository.
- Jenkins retrieved the code from the `main` branch.
- The build step executed the shell script.
- The console displayed `Hello, Jenkins!` and the build finished with `SUCCESS`.

---

## Technologies Used

- Jenkins
- GitHub
- Git
- Shell Scripting
- Continuous Integration (CI)

---

## Conclusion

Successfully created and executed a Jenkins Freestyle job that retrieved source code from GitHub, executed a shell script, and verified a successful build through the Jenkins console output.
