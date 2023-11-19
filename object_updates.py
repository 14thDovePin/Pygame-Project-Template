def _object_updates(self):
    """Process object updates."""
    # Update current frame.
    if self.current_frame < 60:
        self.current_frame += 1
    else:
        self.current_frame = 0

    cf = self.current_frame

    self.orbiting_ship.update(cf)
