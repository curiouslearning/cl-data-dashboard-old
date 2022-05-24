# Cl-Data-Dashboard

A container for a series of visualizations pulling data together across the Curious Learning Ecosystem

## Developer Instructions

### Prerequisites and Dev environment

Docker Desktop

CLIs
- kubectl
- helm

### Running the Development Environment

1. Ensure Docker Desktop is running.

2. Open a terminal instance and run 

    `cd {path/to/project}/dev`
3. from the `/dev` directory run `./dev-env.sh` to build the local cluster
4. from the `/dev` directory run `./dev.sh` to build the project and install it on the local cluster
5. Follow the terminal prompts to begin port-forwarding the container to make it accessible to your browser's localhost
6. repeat steps 4 and 5 each time you wish to deploy a new version of the project 