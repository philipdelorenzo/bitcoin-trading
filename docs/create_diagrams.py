"""This module is built to create a design builder for the project."""
import os
from docs.create_diagrams import Diagram, Cluster
from diagrams.generic.os import Ubuntu, Raspbian, Debian, RedHat, Centos
from diagrams.programming.framework import FastAPI, Flask, Django, React
from diagrams.onprem.inmemory import Redis
from diagrams.programming.language import Python, Bash
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.monitoring import Prometheus 
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.logging import Loki
from diagrams.onprem.network import Istio, Traefik, Pfsense, Internet, Ambassador
from diagrams.onprem.queue import Rabbitmq, Celery
from diagrams.onprem.vcs import Github
from diagrams.onprem.gitops import Argocd
from diagrams.generic.storage import Storage

BASE = os.path.abspath(os.path.dirname(__file__))
diagram_dir = os.path.join(BASE, "diagrams")
diafile = os.path.join(diagram_dir, "bitcoin_trading_api")

if not os.path.exists(diagram_dir):
    os.makedirs(diagram_dir)

# Create a diagram of the Bitcoin Trading API
with Diagram("Bitcoin Trading Application Network", show=False, outformat="jpg", filename=diafile) as diag:
    with Cluster("Internal Network"):
        frontend = Internet("Streamlit Frontend")

        with Cluster("Data Abstraction Layer - ETL"):
            data_abstraction = [Python("ETL")]

        with Cluster("Backend Group"):
            redis_cache = Redis("Redis Cache")
            backend = FastAPI("Backend API")

        # This is used to create the strategy, and test
        with Cluster("Data and Strategy Processing"):
            strategy = FastAPI("Backend Testing API")
            with Cluster("Data Processing Group"):
                dp_group = [
                    Python("TA-Lib"),
                    Python("Pandas"),
                    Python("Numpy"),
                    Python("VectorBT"),
                    Python("Yahoo Finance API"),
                    ]
        
        backend << redis_cache
        backend >> redis_cache
        backend << frontend
        backend >> frontend
        data_abstraction >> redis_cache
        data_abstraction << redis_cache
        strategy >> dp_group
        strategy >> redis_cache
        redis_cache >> strategy
