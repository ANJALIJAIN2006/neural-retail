def simple_feature_importance(feature_names):
    return [{"feature": f, "importance": round(1.0 / (i + 1), 3)} for i, f in enumerate(feature_names)]