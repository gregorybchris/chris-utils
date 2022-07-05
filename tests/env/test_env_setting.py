import pytest

from chris.utils.env import EnvSetting


class TestEnvSetting:
    def test_get_name(self):
        setting = EnvSetting("ENV_SETTING_VAR")
        assert setting.var == "ENV_SETTING_VAR"

    def test_get_value(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("ENV_SETTING_VAR", "env-val")
        setting = EnvSetting("ENV_SETTING_VAR")
        assert setting.value == "env-val"

    def test_get_default_found(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("ENV_SETTING_VAR", "env-val")
        setting = EnvSetting("ENV_SETTING_VAR", default="default-val")
        assert setting.value == "env-val"

    def test_get_default_missing(self):
        setting = EnvSetting("ENV_SETTING_VAR", default="default-val")
        assert setting.value == "default-val"

    def test_optional_missing(self):
        setting = EnvSetting("ENV_SETTING_VAR")
        assert setting.value is None

    def test_required_missing(self):
        setting = EnvSetting("ENV_SETTING_VAR", optional=False)
        with pytest.raises(EnvironmentError, match="Environment variable ENV_SETTING_VAR is not set"):
            print(setting.value)
