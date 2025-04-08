class DataStoreInterface:
    def get_all(self, resource):
        """
        Retrieve all records of the specified resource.

        Args:
            resource (str): The name or identifier of the resource to retrieve.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.

        Returns:
            None: This is a placeholder method and does not return any value.
        """
        raise NotImplementedError

    def get(self, resource, id):
        """
        Retrieve a specific resource by its unique identifier.

        Args:
            resource (str): The name or type of the resource to retrieve.
            id (int or str): The unique identifier of the resource.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.

        Returns:
            Any: The retrieved resource. The return type depends on the implementation.
        """
        raise NotImplementedError

    def add(self, resource, data):
        """
        Adds a new resource with the provided data to the datastore.

        This method should be implemented by subclasses to define the specific
        behavior for adding resources to the datastore.

        Args:
            resource (str): The name or identifier of the resource to be added.
            data (dict): A dictionary containing the data for the resource.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError

    def update(self, resource, id, new_data):
        """
        Update an existing resource in the datastore with new data.

        Args:
            resource (str): The name or type of the resource to update.
            id (int or str): The unique identifier of the resource to be updated.
            new_data (dict): A dictionary containing the updated data for the resource.

        Raises:
            NotImplementedError: This method must be implemented in a subclass.
        """
        raise NotImplementedError

    def delete(self, resource, id):
        """
        Deletes a resource with the specified ID.

        This method should be implemented by subclasses to define the logic
        for deleting a resource from the datastore.

        Args:
            resource (str): The name or type of the resource to delete.
            id (int or str): The unique identifier of the resource to delete.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError