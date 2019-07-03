def test_valid(cldf_dataset, cldf_logger):
    assert any(r['Value'] == 'ezandə kɨ-' for r in cldf_dataset['FormTable'])
    assert cldf_dataset.validate(log=cldf_logger)
