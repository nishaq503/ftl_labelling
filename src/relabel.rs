use ndarray::prelude::*;

#[derive(Debug, Clone)]
pub enum Connectivity {
    One = 1,
    Two = 2,
    Three = 3,
}

#[derive(Debug, Clone)]
struct Polygon {}

#[derive(Debug, Clone)]
pub struct PolygonSet {
    connectivity: Connectivity,
    objects: Vec<Polygon>,
}

impl PolygonSet {
    pub fn new(connectivity: Connectivity) -> Self {
        PolygonSet {
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
        let (y_min, x_min, z_min) = start;
        let (y_max, x_max, z_max) = stop;

        for y in 0..(y_max - y_min) {
            for x in 0..(x_max - x_min) {
                for z in 0..(z_max - z_min) {
                    if x == y && y == z {
                        tile[[y, x, z]] = 1;
                    }
                }
            }
        }
    }
}
