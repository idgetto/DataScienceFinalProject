from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import math
import numpy as np
    
def get_polygon_angles(n_sides):
    interior_angle = (180 * (n_sides - 2)) / float(n_sides)
    exterior_angle = 180 - interior_angle
    
    initial_angle = 90
    angles = [(x * exterior_angle + initial_angle) % 360 for x in range(n_sides+1)]
    
    return angles

def get_polygon_points(angles, radius):
    points = [get_polygon_point(angle, radius) for angle in angles]
    return points

def get_polygon_point(angle, radius):
    x = radius * math.cos(angle * (math.pi/180))
    y = radius * math.sin(angle * (math.pi/180))
    return (x, y)

def get_data_points(angles, values, radius):
    value_radii = [value * radius for value in values]
    value_points = [get_polygon_point(angle, value) for (angle, value) in zip(angles, value_radii)]
#     value_points.append(value_points[0]) # make a loop
    return value_points

def draw_axes(labels):
    angles = get_polygon_angles(len(labels))
    radius = 100
    
    # plot nested polygons
    for inner_radius in np.linspace(0, radius, 4):
        points = get_polygon_points(angles, inner_radius)
        x, y = zip(*points)
        plt.plot(x, y, color='black')

        # draw dotted lines
        outer_points = get_polygon_points(angles, radius)
        for (x, y) in outer_points:
            plt.plot([0, x], [0, y], color='black', ls='--')
            points = np.asarray(outer_points)
            pgon = Polygon(points, color='black', closed=True, alpha=0.1)
     
    # label features
    label_points = get_polygon_points(angles, radius * 1.2)
    for (point, feature) in zip(label_points, labels):
        x, y = point
        plt.text(x, y, feature, fontsize=14, ha='center', va='center')
    
    # remove unnecessary plot things
    plt.axis('equal')
    plt.axis('off')
    plt.grid(False)
    plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
            
def plot_data(values):
    angles = get_polygon_angles(values.shape[1])
    radius = 100
    
    # scale the data
    max_value = float(values.values.max())
    values = values.apply(lambda x: [value / max_value for value in x])
        
    # plot data values
    opacity = 50 / float(len(values))
    for row in values.iterrows():
        value_points = get_data_points(angles, row[1].values, radius)
        points = np.asarray(value_points)
        
        pgon = Polygon(points, closed=True, alpha=opacity)
        plt.gca().add_patch(pgon)
        
    # show max value
    angle = (angles[0] + angles[-2]) / 2.0
    x, y = get_polygon_point(angle, 0.9*radius)
    plt.text(x, y, str(int(max_value)), fontdict={'fontsize':14})

def students_spider_plot(student_ids):
    import pandas as pd
    students = pd.read_csv('../data/student.csv')
    
    selected = students[students.studentid.isin(student_ids)]
    cols = ['me', 'ece', 'design', 'cs', 'bio']
    values = selected[cols]
    
    feature_labels = ['ME', 'ECE', 'DESIGN', 'CS', 'BIO']
    draw_axes(feature_labels)
    
    plot_data(values)

    
def spider_plot(features, values, draw_axes=True):    
    angles = get_polygon_angles(len(features))
    radius = 100
    
    if draw_axes:
        # plot nested polygons
        for inner_radius in np.linspace(0, radius, 4):
            points = get_polygon_points(angles, inner_radius)
            x, y = zip(*points)
            plt.plot(x, y, color='black')

        # draw dotted lines
        outer_points = get_polygon_points(angles, radius)
        for (x, y) in outer_points:
            plt.plot([0, x], [0, y], color='black', ls='--')
        points = np.asarray(outer_points)
        pgon = Polygon(points, color='black', closed=True, alpha=0.1)
        # plt.gca().add_patch(pgon)
        
    # plot data values
    value_points = get_data_points(angles, values, radius)
    points = np.asarray(value_points)
    pgon = Polygon(points, closed=True, alpha=0.05)
    plt.gca().add_patch(pgon)
    
    # label features
    label_points = get_polygon_points(angles, radius * 1.2)
    for (point, feature) in zip(label_points, features):
        x, y = point
        plt.text(x, y, feature, fontsize=14, ha='center', va='center')

    x, y = zip(*outer_points)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    plt.xlim((xmin-20,xmax+20))
    plt.ylim((ymin-20,ymax+50))
        
    # remove unnecessary plot things
    plt.axis('equal')
    plt.axis('off')
    plt.grid(False)
    plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')