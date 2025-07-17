variable "name" {
  type        = string
  description = "Name of the disk"
}

variable "type" {
  type        = string
  description = "Disk type (e.g., pd-standard, pd-ssd)"
}

variable "zone" {
  type        = string
  description = "Zone where disk will be created"
}

variable "size" {
  type        = number
  description = "Size of the disk in GB"
}
