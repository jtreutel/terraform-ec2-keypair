output "key_name" {
  value = aws_key_pair.this.key_name
}
output "fingerprint" {
  value = aws_key_pair.this.fingerprint
}

output "public_key" {
  value = tls_private_key.this.public_key_pem
}
output "public_key_openssh" {
  value = tls_private_key.this.public_key_openssh
}
output "private_key" {
  value = tls_private_key.this.private_key_pem
}



