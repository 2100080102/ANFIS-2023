import numpy as np
def euclidean distance(point1, point2)
#Calculate the Euclidean distance between two points in 20 space.
  return np.linalg.norm(np.array(point1)-np.array(point2))
def nearest_neighbor_tsp(points)
"""Solve the Traveling Salesman Froblem using the nearest neighbor algorithm.
Args:
points: A list tuples representing the coordinates of cities
Returns
tour A list representing the order in which cities should be visited.
total distance The total distance of the tour."""
mum_cities=len(points)
unvisited_cities=set(range(num_cities))
current_city=0 #Start from the first city 
tour=[current_city]
total_distance=0
while len(tour)<num_cities:
  nearest_city =min(unvisited_cities, key=lambda city:exclidean_distance(points[current_city), points[city]))
  total_distance+= euclidean_distance(points[current_city], points[nearest_city])
  current_city =nearest_city 
  tour.append(current_city)
  unvisited_cities.remove(current_city)
#Return to the starting city to complete the tour.
total_distance+= euclidean_distance(points[current_city], points [tour[0]])
tour.append(tour[0])
return tour, total_distance
#Example usage:
cities=[(0, 0), (2, 4), (3, 1), (5, 3), (6, 6)] 
tour, total_distance=nearest_neighbor_tsp(cities)
print("Optimized Tour Order:", tour)
print("Total Distance:", total_distance)
