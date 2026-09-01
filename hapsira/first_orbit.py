from astropy import units as u
from hapsira.bodies import Earth
from hapsira.twobody import Orbit
from hapsira.plotting import OrbitPlotter

# Classical orbital elements for a satellite in a roughly ISS-like orbit
a = 6798 * u.km       # semi-major axis: average distance from Earth's center
ecc = 0.0003 * u.one   # eccentricity: how "squished" the orbit is (0 = circle)
inc = 51.6 * u.deg     # inclination: tilt of the orbit relative to the equator
raan = 0 * u.deg       # right ascension of ascending node: where orbit crosses equator going north
argp = 0 * u.deg       # argument of periapsis: orientation of the ellipse within the orbital plane
nu = 0 * u.deg         # true anomaly: where the satellite currently sits along the orbit

orbit = Orbit.from_classical(Earth, a, ecc, inc, raan, argp, nu)

# Propagate forward by a quarter of the orbital period
quarter_period = orbit.period / 4
future_orbit = orbit.propagate(quarter_period)

print("Original orbit:", orbit)
print("Orbital period:", orbit.period.to(u.min))
print("Position after a quarter period:", future_orbit.r)

#print(orbit)

plotter = OrbitPlotter()
plotter.plot(orbit, label="t = 0")
plotter.plot(future_orbit, label="t = quarter period")
plotter.show()