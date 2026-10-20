
# Exercise 4 — Docker Networking with Multiple Containers

## 1. Flask Docker Image Build and Initial API Test

The Flask application was successfully containerized, and the `flask-api` Docker image was built successfully.

![Flask Docker Image Build](https://raw.githubusercontent.com/yashraj7774/DEVOPS-EXERCISE/main/exercise4/flask-image-build.png)

---

## 2. Container-to-Container Communication

The Flask container successfully resolved and communicated with the MySQL and Redis containers through the `my-bridge-net` Docker bridge network.

![Container Networking](https://raw.githubusercontent.com/yashraj7774/DEVOPS-EXERCISE/main/exercise4/container-networking.png)

---

## 3. MySQL Database Verification

The MySQL container was successfully initialized with the `devopsdb` database.

![MySQL Verification](https://raw.githubusercontent.com/yashraj7774/DEVOPS-EXERCISE/main/exercise4/mysql-verification.png)

---

## 4. Final Multi-Container Configuration

The final configuration consisted of the Flask, MySQL, and Redis containers running on the same Docker bridge network, enabling communication between the containers.

![Final Docker Network](https://raw.githubusercontent.com/yashraj7774/DEVOPS-EXERCISE/main/exercise4/final-network-state.png)

---

## Technologies Used

- Docker
- Docker Bridge Networking
- Flask
- MySQL
- Redis

---

## Conclusion

Successfully built a Flask Docker image, configured a custom Docker bridge network, verified communication between Flask, MySQL, and Redis containers, and confirmed the final multi-container network configuration.
