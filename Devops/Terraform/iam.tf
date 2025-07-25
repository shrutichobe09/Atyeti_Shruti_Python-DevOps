<<<<<<< HEAD
resource "aws_iam_role" "eks_role" {
 name = "eks-cluster-role"
 assume_role_policy = jsonencode({
 Version = "2012-10-17"
 Statement = [{

 Action = "sts:AssumeRole"
 Effect = "Allow"
 Principal = {
 Service = "eks.amazonaws.com"
 }
 }]
 })
 tags = {
 Name = "eks-role"
 }
}
resource "aws_iam_role_policy_attachment" "eks_policy" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
 role = aws_iam_role.eks_role.name
=======
resource "aws_iam_role" "eks_role" {
 name = "eks-cluster-role"
 assume_role_policy = jsonencode({
 Version = "2012-10-17"
 Statement = [{

 Action = "sts:AssumeRole"
 Effect = "Allow"
 Principal = {
 Service = "eks.amazonaws.com"
 }
 }]
 })
 tags = {
 Name = "eks-role"
 }
}
resource "aws_iam_role_policy_attachment" "eks_policy" {
 policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
 role = aws_iam_role.eks_role.name
>>>>>>> e3c1d965699b0c4f4860543bea638f73d9954c75
}