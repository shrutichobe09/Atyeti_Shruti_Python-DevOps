output "vpc_name" {
    value = google_compute_network.custom_vpc.name
  
}

output "public_subnet_cidr" {
    value = google_compute_subnetwork.public_subnet.ip_cidr_range
  
}

output "private_subnet_cidr" {
    value = google_compute_subnetwork.private_subnet.ip_cidr_range
  
}