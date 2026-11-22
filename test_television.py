import pytest
from television import Television

class Test:
    """Test Television class functions"""
    def setup_method(self):
        """Set up a new Television object for each test."""
        self.tv1 = Television()

    def teardown_method(self) -> None:
        """Teardown the new Television after each test."""
        del self.tv1

    def test_init(self) -> None:
        """Test the initialization of Television object for desired parameters."""
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self) -> None:
        """Test the power function for Television object.

        Verifies that Television is powered on and off when power function is called.
        """
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self) -> None:
        """Test the mute function for Television object for desired parameters.

        Verifies that mute only works when Television is powered on.
        """
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_up(self) -> None:
        """Verifies that channel increases only when Television is powered on.

        Verifies that the channel wraparound works when going up from the highest channel.
        """
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 2, Volume = 0'

        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self) -> None:
        """Verifies that channel decreases only when Television is powered on.

        Verifies that the channel wraparound works when going down from the lowest channel.
        """
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 2, Volume = 0'

        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self) -> None:
        """Verifies that volume increases only when Television is powered on.
        """
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self) -> None:
        """Verifies that volume decreases only when Television is powered on.
        """
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'