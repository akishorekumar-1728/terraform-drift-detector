def detect_drift(terraform_output):

    if "Objects have changed outside of Terraform" in terraform_output:
        return True

    if "will be created" in terraform_output:
        return True

    if "will be destroyed" in terraform_output:
        return True

    if "will be updated" in terraform_output:
        return True

    return False