provider "google" {
  #credentials = file(var.credentials_file)
  project = var.project_id
  region = var.region
  zone = var.zone
}

#reserve static ip
resource "google_compute_address" "static_ip" {
  name   = "vm-static-ip"
  region = var.region
}


resource "google_compute_instance" "vm_instance" {
  name             = "demo-vm"
  zone             = var.zone
  machine_type     = "e2-micro"



  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      labels = {
        my_label = "value"
      }
    }
  }


  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }
  
 
}