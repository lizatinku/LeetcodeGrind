# My plan
# Step 1:
# Initialize a dictionary to represent the adjacency list of the graph
# Each key is a course, and the value is a list of courses that depend on it
# Create an array to track the in-degree (number of prerequisites) for each course
# For each prerequisite pair, add an edge from prerequisite to course
# Increment the in-degree of the course since it has one more prerequisite
# Step 2
# Initialize the queue with courses having in-degree 0
# Create a queue and add all courses with no prerequisites (in-degree 0)
# Step 3
# Initialize a counter to track how many courses have been visited/processed
# Remove a course from the front of the queue
# Iterate over all the courses that depend on the current course
# Reduce the in-degree of the neighbor by 1, as we've processed one prerequisite
# If the in-degree of the neighbor becomes 0, add it to the queue
# Step 4
# Check if all courses were visited

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        visited = 0
        while queue:
            current = queue.popleft()
            visited += 1
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited == numCourses