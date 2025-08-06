provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_kms_key_ring" "vault_ring" {
  name     = var.kms_keyring
  location = var.region
}

resource "google_kms_crypto_key" "vault_key" {
  name            = var.kms_key
  key_ring        = google_kms_key_ring.vault_ring.id
  rotation_period = "100000s"
}

resource "google_compute_network" "vault_net" {
  name = "vault-prod-vpc"
}

resource "google_compute_firewall" "vault_firewall" {
  name    = "vault-fw"
  network = google_compute_network.vault_net.name

  allow {
    protocol = "tcp"
    ports    = ["8200", "22"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_service_account" "vault_sa" {
  account_id   = "vault-service-account"
  display_name = "Vault SA"
}

resource "google_project_iam_member" "kms_decrypt" {
  project = var.project_id
  role   = "roles/cloudkms.cryptoKeyDecrypter"
  member = "serviceAccount:${google_service_account.vault_sa.email}"
}

resource "google_compute_instance" "vault" {
  name         = var.instance_name
  machine_type = "e2-medium"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "ubuntu-2204-lts"
      size  = 20
    }
  }

  network_interface {
    network = google_compute_network.vault_net.name
    access_config {}
  }

  service_account {
    email  = google_service_account.vault_sa.email
    scopes = ["cloud-platform"]
  }

  metadata_startup_script = file("startup.sh")

  tags = ["vault"]
}
