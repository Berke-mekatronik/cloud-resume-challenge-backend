variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "S3 bucket name for resume website"
  type        = string
}

variable "dynamodb_table_name" {
  description = "DynamoDB table for visitor counter"
  type        = string
  default     = "cloud-resume-visitors"
}

