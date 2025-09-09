def check_migration_warning(type_parcours: str) -> bool:
    """Return True if the type_parcours hints at a migration use case."""
    if not type_parcours:
        return False
    migration_keywords = ['migration', 'migrer', 'migrer un parcours', 'migration parcours']
    tp = type_parcours.lower()
    return any(k in tp for k in migration_keywords)


