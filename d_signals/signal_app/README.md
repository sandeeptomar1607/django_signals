Model signals - A set of signals sent by the model system.

i. pre_init(sender, args, kwargs) - Whenever you instantiate a Django model, this signal is sent at the beggining of the model's __init__() method.

    sender: The model class that just had an instance created.
    args: A list of positional arguments passed to __init__().
    kwargs: A dictionary of keyword arguments passed to __init__().

ii. post_init(sender, instance) - Like pre_init, but this one is sent when __init__() mehtod finishes.

iii. pre_save(sender, instance, raw, using, update_fields) - This is sent at the beggining of the model's save() method.

    sender: The model class.
    instance: The actual isntance being saved.
    raw: A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). One should not query/modify other records in the database as the database might not be in the consistent state yet.
    using: The databse alias being used.
    update_fields: The set of feilds to update as passed to Model.save(), or None if not passed.

iv. post_save(sender, instance, created, raw, using, update_fields) - Like pre_save, but sent at te end of the save() method.
    
    created - A boolean; True if a new record was created.

v. pre_delete(sender, instance, using) - Sent at the beggining of a model's delete() method and a queryset's delete() method.
