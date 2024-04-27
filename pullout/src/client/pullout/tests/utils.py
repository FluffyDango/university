def check_valid_list(self, found, all_items):
    verified_items = []
    for item in found:
        if item in all_items:
            verified_items.append(item)
    
    result = [item for item in all_items if item not in verified_items]

    if result:
        err_msg = "Failed to find " + str(result) + " but found: " + str(found)
        self.fail(err_msg)

def check_invalid_list(self, found, all_items):
    result = [item for item in found if item in all_items]

    if result:
        err_msg = "Found invalid items " + str(result)
        self.fail(err_msg)