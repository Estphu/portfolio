from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="ESTPHU",
    settings_files=["settings.yaml", ".secrets.yaml"],
    environments=True,
)

# `envvar_prefix` = export envvars with `export ESTPHU_FOO=bar`.
# `settings_files` = Load these files in the order.
