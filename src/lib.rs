mod relabel;

use numpy::PyReadonlyArray3;
use numpy::PyArray3;
use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone)]
pub struct PolygonSet {
    polygon_set: relabel::PolygonSet,
}

#[pymethods]
impl PolygonSet {
    #[new]
    pub fn new(connectivity: u8) -> Self {
        let connectivity = match connectivity {
            1 => relabel::Connectivity::One,
            2 => relabel::Connectivity::Two,
            3 => relabel::Connectivity::Three,
            _ => panic!(
                "Connectivity must be 1, 2 or 3. Got {} instead.",
                connectivity
            ),
        };
        Self {
            polygon_set: relabel::PolygonSet::new(connectivity),
        }
    }

    pub fn num_objects(&self) -> usize {
        self.polygon_set.num_objects()
    }

    pub fn add_tile(
        &mut self,
        tile: PyReadonlyArray3<bool>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        self.polygon_set.add_tile(tile.as_array(), start, stop);
    }

    pub fn digest(&mut self) {
        self.polygon_set.digest();
    }

    pub fn extract_tile(
        &self,
        tile: &PyArray3<u32>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        let tile = unsafe { tile.as_array_mut() };
        self.polygon_set.extract_tile(tile, start, stop);
    }
}

#[pymodule]
fn ftl_labelling(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<PolygonSet>()?;

    Ok(())
}
