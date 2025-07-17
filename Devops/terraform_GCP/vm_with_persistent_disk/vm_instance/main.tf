resource "google_compute_instance" "vm_instance" {
  name         = var.name
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = var.image
    }
  }

  network_interface {
    network    = var.network
    subnetwork = var.subnetwork
    access_config {}
  }

  attached_disk {
    source      = var.disk_self_link
    device_name = "persistent-disk-1"
    mode        = "READ_WRITE"
  }

  metadata = {
    ssh-keys = "terraform:${file(var.public_key_path)}"
  }
}
