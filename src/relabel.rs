use ndarray::prelude::*;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Connectivity {
    One = 1,
    Two = 2,
    Three = 3,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Run {
    z: usize,
    y: usize,
    start: usize,
    stop: usize,
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct Object {
    connectivity: Connectivity,
    runs: Vec<Run>,
    start: (usize, usize, usize), // bottom, left,  deep
    stop: (usize, usize, usize),  // top,    right, high
}

impl Ord for Object {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl PartialOrd for Object {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        match self.start.cmp(&other.start) {
            std::cmp::Ordering::Less => Some(std::cmp::Ordering::Less),
            std::cmp::Ordering::Equal => Some(self.stop.cmp(&other.stop)),
            std::cmp::Ordering::Greater => Some(std::cmp::Ordering::Greater),
        }
    }
}

#[derive(Debug, Clone)]
pub struct ObjectSet {
    connectivity: Connectivity,
    objects: Vec<Object>,
}

impl ObjectSet {
    pub fn new(connectivity: Connectivity) -> Self {
        ObjectSet {
            connectivity,
            objects: Vec::new(),
        }
    }

    pub fn num_objects(&self) -> usize {
        self.objects.len()
    }

    pub fn add_tile(
        &mut self,
        tile: ArrayView3<bool>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        println!(
            "hello from Rust add_tile! {:?}, {:?}, {:?}",
            tile.shape(),
            start,
            stop
        );
    }

    pub fn digest(&mut self) -> usize {
        println!(
            "hello from Rust digest! Connectivity is {:?}",
            self.connectivity
        );
        self.num_objects()
    }

    pub fn extract_tile(
        &self,
        mut tile: ArrayViewMut3<u32>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        println!(
            "hello from Rust extract_tile! {:?}, {:?}, {:?}",
            tile.shape(),
            start,
            stop
        );
        let (z_min, y_min, x_min) = start;
        let (z_max, y_max, x_max) = stop;

        for z in 0..(z_max - z_min) {
            for y in 0..(y_max - y_min) {
                for x in 0..(x_max - x_min) {
                    if x == y && y == z {
                        tile[[y, x, z]] = 1;
                    }
                }
            }
        }
    }
}
