# 3-tier containers in OCP


Architecture:


Container 1: React UI (Port 3000)


Container 2: Python API / Middleware Server (Port 5000)


Container 3: Database (e.g., PostgreSQL, Port 5432)


Step1: Describe Project Structure

3-tier/
├── ui/
│   ├── Dockerfile
│   ├── public/
│   └── src/
├── api/
│   ├── Dockerfile
│   └── app.py
└── db/
    └── Dockerfile



Step2: Setup Dockerfiles for UI, Middleware and Database




Step3: Source Code for Application




Step4: Build and push images to the registry



Step5: Deployment to openshift 
  -> Deploy YAML in Openshift 


Step 6: Expose UI Services
 -> oc expose svc/ui

 
 

 Step7: Setup openshift to deploy
 -> Login to OCP
 -> Create project 
 -> Apply Configuration


Step 8: Inplement CI/CD to automate the entire process


Pre-req:
    -> OCP cluster with OCP pipelines installed
    -> git repo for the application code
    -> docker registry to push images



SET UP Openshift Project

-> Create a new project
-> Setup Tekton CI
        ---install tekton pipeline in openshift
        ---Create Tekton Pipeline
        ----
-> Setup ArgoCD
-> Automate Deployments with Webhook
-> 




 







