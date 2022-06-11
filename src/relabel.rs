use ndarray::prelude::*;

#[derive(Debug)]
pub enum Connectivity {
    One = 1,
    Two = 2,
    Three = 3,
}

#[derive(Debug)]
struct Polygon {}

#[derive(Debug)]
pub struct PolygonSet {
    connectivity: Connectivity,
    objects: Vec<Polygon>
}

impl PolygonSet {
    pub fn new(connectivity: Connectivity) -> Self {
        PolygonSet { connectivity, objects: Vec::new() }
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
        println!("hello from Rust add_tile!")
    }

    pub fn digest(&mut self) {
        println!("hello from Rust digest!")
    }

    pub fn extract_tile(
        &self,
        tile: ArrayViewMut3<u32>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        println!("hello from Rust extract_tile!")
    }
}
