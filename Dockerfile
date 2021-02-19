# Dockerfile

FROM continuumio/miniconda:4.7.12
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "my-rdkit-env", "/bin/bash", "-c"]

# Activate the environment, and make sure it's activated:
RUN echo "Making sure rdkit is installed:"
RUN python -c "from rdkit import Chem"

# The code to run when container is started:
ADD herg_docker.py .
ADD rf.pkl .
ADD xgb.pkl .
ENTRYPOINT ["conda", "run", "-n", "my-rdkit-env", "python", "herg_docker.py"]
