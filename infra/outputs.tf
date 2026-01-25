output "cloudfront_url" {
  description = "Resume CloudFront URL"
  value       = aws_cloudfront_distribution.resume_cdn.domain_name
}

output "api_gateway_url" {
  description = "Visitor counter API endpoint"
  value       = "${aws_api_gateway_stage.prod.invoke_url}/count"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.resume_bucket.bucket
}
