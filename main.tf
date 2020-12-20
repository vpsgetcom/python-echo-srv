terraform {
  required_providers {
    docker = {
      source = "terraform-providers/docker"
    }
  }
}

provider "docker" {
  host    = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "python-echo-server" {
  name         = "ndidocker/echo-server:latest"
  keep_locally = false
}

resource "docker_container" "python-echo-server" {
  image = docker_image.echo-server.latest
  name  = "tutorial"
  ports {
    internal = 4444
    external = 4444
  }
}
