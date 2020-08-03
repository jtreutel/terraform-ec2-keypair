# tf-module-ec2-key-pair

Creates an AWS keypair.  There's currently no Terraform module that will do this for you.


### Module Inputs

|Name|Type|Default|Notes|
|---|---|---|---|
|key_name|`string`|none|Desired name of AWS EC2 key pair.|


### Module Outputs
|Name|Notes|
|---|---|
|key_name           |The AWS resource name of the key pair. |
|private_key        |The private key in PEM format.         |
|public_key         |The public key in PEM format.          |
|public_key_openssh | The public key in OpenSSH format, e.g. _ssh-rsa AAAAB3N..._       |
|fingerprint        |The MD5 public key fingerprint, e.g. _f6:fc:1c:03:17:..._          |


### Example Module Declaration

```
module "webserver_key" {
    source   = "git::https://github.com/jtreutel/terraform-ec2-keypair.git"
    key_name = "web"
}
resource "local_file" "webserver_key_private" {
    content         = module.webserver_key.private_key
    filename        = "${path.root}/webserver_key.pem"
    file_permission = "0600"
}
resource "local_file" "webserver_key_public" {
    content  = module.webserver_key.public_key
    filename = "${path.root}/webserver_key.pub"
}

resource "aws_instance" "webserver" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"
  key_name      = module.webserver_key.key_name
}
```

