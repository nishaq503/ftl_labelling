mod relabel;

use numpy::{PyArray3, PyReadonlyArray3};
use pyo3::prelude::*;

#[pyclass]
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
            _ => panic!("Connectivity must be 1, 2 or 3. Got {} instead.", connectivity),
        };
        Self { polygon_set: relabel::PolygonSet::new(connectivity) }
    }

    pub fn num_objects(&self) -> usize {
        self.polygon_set.num_objects()
    }

    pub fn add_tile(
        &mut self,
        // _py: Python<'_>,
        tile: &PyArray3<bool>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        let tile = unsafe { tile.as_array() };
        self.polygon_set.add_tile(tile, start, stop);
    }

    pub fn digest(&mut self) {
        self.polygon_set.digest();
    }

    pub fn extract_tile(
        &self,
        // _py: Python<'_>,
        tile: PyReadonlyArray3<u32>,
        start: (usize, usize, usize),
        stop: (usize, usize, usize),
    ) {
        let tile = unsafe { tile.as_array_mut() };
        self.polygon_set.extract_tile(tile, start, stop);
    }
}

// #[pyfunction]
// pub fn drop_polygon_set<'py>(_py: Python<'py>, polygon_set: PolygonSet) -> PyResult<()> {
//     Ok(())
// }

#[pymodule]
fn ftl_labelling(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<PolygonSet>()?;

    Ok(())
}
