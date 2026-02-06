def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    result = []
    for request in requests:
        user_id = request.get("user_id")
        online_feature = request.get("online_features", {})

        offline_feature = feature_store.get(user_id, defaults)

        result.append({**online_feature, **offline_feature})

    return result

    