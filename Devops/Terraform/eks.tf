module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.21.0"

  cluster_name    = "eks_cluster"
  cluster_version = "1.31"

  vpc_id     = aws_vpc.eks_vpc.id
  subnet_ids = [
    aws_subnet.public_subnet.id,
    aws_subnet.private_subnet.id
  ]

cluster_endpoint_public_access  = true
cluster_endpoint_private_access = true


  tags = {
    Name = "eks_cluster"
  }
}
