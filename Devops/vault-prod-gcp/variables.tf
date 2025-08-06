variable "project_id" {
  default = "rosy-resolver-465404-b2"
}

variable "region" {
  default = "us-central1"
}

variable "zone" {
  default = "us-central1-a"
}

variable "kms_keyring" {
  default = "vault-keyring"
}

variable "kms_key" {
  default = "vault-key"
}

variable "instance_name" {
  default = "vault-prod"
}
