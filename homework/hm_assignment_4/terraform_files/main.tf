terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.20.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = file(var.credentials)
  project     = var.project_name
  region      = var.region
}

resource "google_storage_bucket" "auto-expire" {
  name          = var.gcp_storage_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "default" {
  dataset_id                  = var.gcp_bigquery_dataset_id
  friendly_name               = var.gcp_bigquery_dataset_name
  location                    = var.location
}
