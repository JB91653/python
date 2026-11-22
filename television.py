class Television:
    """A Television with controls to power on/off, mute/unmute, channel up/down, volume up/down.
    """
    MIN_VOLUME = 0 # Television lower volume limit
    MAX_VOLUME = 2 # Television upper volume limit
    MIN_CHANNEL = 0 # Television lower channel limit
    MAX_CHANNEL = 3 # Television upper channel limit

    def __init__(self) -> None:
        """Initialize a new Television object with the following:
        Powered off
        Unmuted
        Volume level at 0
        Tuned to channel 0
        Pre-mute volume level 0
        """
        self.__status = False # Television power on/off status
        self.__muted = False # Television mute status
        self.__volume = Television.MIN_VOLUME # Initial Television volume
        self.__channel = Television.MIN_CHANNEL # Initial Television channel
        self.__mute_volume = Television.MIN_VOLUME # Store pre-muted volume level to return to on unmute

    def power(self) -> None:
        """Power the Television on or off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """Mute or unmute the Television.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__mute_volume # Restores pre-mute volume
            else:
                self.__muted = True
                self.__mute_volume = self.__volume # Stores volume prior to muting Television
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """Adjust the Television channel up.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Adjust the Television channel down.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Adjust the Television volume up.

        If the Television is muted, it automatically unmutes prior to volume up adjustment.
        """
        if self.__status:
            if self.__muted:
                self.mute() # Calls mute function to restore pre-mute volume level prior to volume adjustment
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Adjust the Television volume down.

        If the Television is muted, it automatically unmutes prior to volume down adjustment.
        """
        if self.__status:
            if self.__muted:
                self.mute() # Calls mute function to restore pre-mute volume level prior to volume adjustment
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the Television power status, current channel, and current volume.

        Example: Power = False, Channel = 0, Volume = 0
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
