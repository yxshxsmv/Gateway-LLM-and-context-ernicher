def demo_only(payload):
    import pickle
    import subprocess
    import yaml

    pickle.loads(payload)
    yaml.unsafe_load(payload)
    subprocess.run(payload, shell=True)
