provider "google" {
    project = var.project_id
    region = var.region
  
}

#create custom network 
resource "google_compute_network" "custom_vpc" {
    name = "custom-vpc"
    auto_create_subnetworks = false
  
}

#public subnet
resource "google_compute_subnetwork" "public_subnet" {
  name = "public-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region = var.region
  network = google_compute_network.custom_vpc.name
}

resource "google_compute_subnetwork" "private_subnet" {
  name = "private-subnet"
  ip_cidr_range = "10.0.2.0/24"
  region = var.region
  network = google_compute_network.custom_vpc.name
}