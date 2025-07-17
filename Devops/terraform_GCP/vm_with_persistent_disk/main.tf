provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

module "disk" {
  source = "./vm"

  name = "my-data-disk"
  type = "pd-standard"
  zone = var.zone
  size = 20
}

module "vm_instance" {
  source = "./vm_instance"

  name            = "my-instance"
  machine_type    = "e2-medium"
  zone            = var.zone
  image           = "debian-cloud/debian-11"
  network         = var.network
  subnetwork      = var.subnetwork
  public_key_path = var.public_key_path
  disk_self_link  = module.disk.disk_self_link
}
