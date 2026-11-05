---
search:
  exclude: true
---

# Phillips_2layer: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [Phillips_2layer](../mom6examples/Phillips_2layer.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = True                    !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">SPLIT_RK2B = False              !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use a version of the split explicit time stepping scheme that</span>
<span id="L8">                                ! exchanges velocities with step_MOM that have the average barotropic phase over</span>
<span id="L9">                                ! a baroclinic timestep rather than the instantaneous barotropic phase.</span>
<span id="L10">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L11">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L12">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L13">ENABLE_THERMODYNAMICS = False   !   [Boolean] default = True</span>
<span id="L14">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L15">USE_EOS = False                 !   [Boolean] default = False</span>
<span id="L16">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L17">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L18">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L19">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L20">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L21">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
<span id="L22">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L23">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L24">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L25">                                ! T&amp;S diagnostics.</span>
<span id="L26">ADIABATIC = False               !   [Boolean] default = False</span>
<span id="L27">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L28">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L29">                                ! eliminating subroutine calls.</span>
<span id="L30">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L31">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L32">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L33">                                ! development</span>
<span id="L34">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L35">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L36">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L37">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L38">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L39">USE_REGRIDDING = False          !   [Boolean] default = False</span>
<span id="L40">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L41">                                ! layered isopycnal algorithm.</span>
<span id="L42">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L43">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L44">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L45">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L46">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L47">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L48">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L49">                                ! edges of the grid cells.</span>
<span id="L50">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L51">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L52">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L53">                                ! points.</span>
<span id="L54">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L55">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L56">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L57">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L58">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L59">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L60">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L61">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L62">DT = 600.0                      !   [s]</span>
<span id="L63">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L64">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L65">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L66">DT_THERM = 1800.0               !   [s] default = 600.0</span>
<span id="L67">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L68">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L69">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L70">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L71">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L72">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L73">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L74">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L75">                                ! equal to DT_THERM.</span>
<span id="L76">DT_TRACER_ADVECT = 1800.0       !   [s] default = 1800.0</span>
<span id="L77">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L78">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L79">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L80">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L81">                                ! DT_THERM.</span>
<span id="L82">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L83">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L84">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L85">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L86">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L87">THICKNESSDIFFUSE = True         !   [Boolean] default = False</span>
<span id="L88">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L89">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L90">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L91">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L92">THICKNESSDIFFUSE_FIRST = False  !   [Boolean] default = False</span>
<span id="L93">                                ! If true, do thickness diffusion or interface height smoothing before dynamics.</span>
<span id="L94">                                ! This is only used if THICKNESSDIFFUSE or APPLY_INTERFACE_FILTER is true.</span>
<span id="L95">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L96">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L97">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L98">                                ! velocities).</span>
<span id="L99">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L100">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L101">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L102">                                ! indicates no averaging.</span>
<span id="L103">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L104">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L105">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L106">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L107">                                ! computed.</span>
<span id="L108">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L109">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L110">                                ! step, using the specified value at the end of the step.</span>
<span id="L111">DTBT_RESET_PERIOD = 8.64E+04    !   [s] default = 1800.0</span>
<span id="L112">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L113">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L114">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L115">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L116">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L117">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L118">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L119">                                ! and odd numbers used for y-first.</span>
<span id="L120">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L121">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L122">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L123">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L124">                                ! first direction can not be found in the restart file.</span>
<span id="L125">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L126">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L127">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L128">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L129">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L130">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L131">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L132">                                ! updated and more robust forms of the same expressions.</span>
<span id="L133">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L134">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L135">IC_OUTPUT_FILE = &quot;MOM_IC&quot;       ! default = &quot;MOM_IC&quot;</span>
<span id="L136">                                ! The file into which to write the initial conditions.</span>
<span id="L137">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L138">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L139">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L140">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L141">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L142">                                ! The file into which to write the ocean geometry.</span>
<span id="L143">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L144">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L145">                                ! analysis and machine-learning inference.</span>
<span id="L146">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L147">                                ! If true, enables the ice shelf model.</span>
<span id="L148">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L149">                                ! If true, use the particles package.</span>
<span id="L150">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L151">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L152">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L153">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L154">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L155">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L156">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L157">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L158">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L159"></span>
<span id="L160">! === module MOM_domains ===</span>
<span id="L161">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L162">                                ! If true, the domain is zonally reentrant.</span>
<span id="L163">REENTRANT_Y = False             !   [Boolean] default = False</span>
<span id="L164">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L165">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L166">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L167">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L168">NIGLOBAL = 60                   !</span>
<span id="L169">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L170">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L171">NJGLOBAL = 80                   !</span>
<span id="L172">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L173">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L174">NIHALO = 4                      ! default = 4</span>
<span id="L175">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L176">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L177">NJHALO = 4                      ! default = 4</span>
<span id="L178">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L179">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L180"></span>
<span id="L181">! === module MOM_hor_index ===</span>
<span id="L182">! Sets the horizontal array index types.</span>
<span id="L183"></span>
<span id="L184">! === module MOM_grid ===</span>
<span id="L185">! Parameters providing information about the lateral grid.</span>
<span id="L186">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L187">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L188"></span>
<span id="L189">! === module MOM_fixed_initialization ===</span>
<span id="L190">INPUTDIR = &quot;INPUT&quot;              ! default = &quot;.&quot;</span>
<span id="L191">                                ! The directory in which input files are found.</span>
<span id="L192"></span>
<span id="L193">! === module MOM_grid_init ===</span>
<span id="L194">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L195">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L196">                                ! grid.  Current options are:</span>
<span id="L197">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L198">                                !              file set by GRID_FILE.</span>
<span id="L199">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L200">                                !     spherical - use a simple spherical grid.</span>
<span id="L201">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L202">AXIS_UNITS = &quot;k&quot;                ! default = &quot;degrees&quot;</span>
<span id="L203">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L204">                                !     degrees - degrees of latitude and longitude</span>
<span id="L205">                                !     m or meter(s) - meters</span>
<span id="L206">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L207">SOUTHLAT = 0.0                  !   [km]</span>
<span id="L208">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L209">                                ! y-axis.</span>
<span id="L210">LENLAT = 1600.0                 !   [km]</span>
<span id="L211">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L212">WESTLON = 0.0                   !   [km] default = 0.0</span>
<span id="L213">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L214">                                ! x-axis.</span>
<span id="L215">LENLON = 1200.0                 !   [km]</span>
<span id="L216">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L217">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L218">                                ! The radius of the Earth.</span>
<span id="L219">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L220">                                ! This specifies how bathymetry is specified:</span>
<span id="L221">                                !     file - read bathymetric information from the file</span>
<span id="L222">                                !       specified by (TOPO_FILE).</span>
<span id="L223">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L224">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L225">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L226">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L227">                                !       wall at the southern face.</span>
<span id="L228">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L229">                                !       profile in the meridional direction.</span>
<span id="L230">                                !     bbuilder - build topography from list of functions.</span>
<span id="L231">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L232">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L233">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L234">                                !       DOME sill-overflow test case.</span>
<span id="L235">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L236">                                !       ISOMIP test case.</span>
<span id="L237">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L238">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L239">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L240">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L241">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L242">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L243">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L244">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L245">                                !     USER - call a user modified routine.</span>
<span id="L246">MINIMUM_DEPTH = 1.0             !   [m] default = 0.0</span>
<span id="L247">                                ! The minimum depth of the ocean.</span>
<span id="L248">MAXIMUM_DEPTH = 2000.0          !   [m]</span>
<span id="L249">                                ! The maximum depth of the ocean.</span>
<span id="L250"></span>
<span id="L251">! === module MOM_open_boundary ===</span>
<span id="L252">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L253">! if any.</span>
<span id="L254">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L255">                                ! The number of open boundary segments.</span>
<span id="L256">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L257">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L258">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L259">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L260">                                ! A parameter that determines which set of channels are</span>
<span id="L261">                                ! restricted to specific  widths.  Options are:</span>
<span id="L262">                                !     none - All channels have the grid width.</span>
<span id="L263">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L264">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L265">                                !     list - Read the channel locations and widths from a</span>
<span id="L266">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L267">                                !       test case.</span>
<span id="L268">                                !     file - Read open face widths everywhere from a</span>
<span id="L269">                                !       NetCDF file on the model grid.</span>
<span id="L270">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L271">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L272">ROTATION = &quot;beta&quot;               ! default = &quot;2omegasinlat&quot;</span>
<span id="L273">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L274">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L275">                                !       times the sine of latitude.</span>
<span id="L276">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L277">                                !     USER - call a user modified routine.</span>
<span id="L278">F_0 = 6.49E-05                  !   [s-1] default = 0.0</span>
<span id="L279">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L280">BETA = 2.0E-11                  !   [m-1 s-1] default = 0.0</span>
<span id="L281">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L282">BETA_LAT_REF = 0.0              !   [kilometers] default = 0.0</span>
<span id="L283">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L284">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L285">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L286">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L287">                                ! arise at the tripolar fold.</span>
<span id="L288"></span>
<span id="L289">! === module MOM_verticalGrid ===</span>
<span id="L290">! Parameters providing information about the vertical grid.</span>
<span id="L291">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L292">                                ! The gravitational acceleration of the Earth.</span>
<span id="L293">RHO_0 = 1031.0                  !   [kg m-3] default = 1035.0</span>
<span id="L294">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L295">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L296">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L297">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L298">                                ! If true, make the Boussinesq approximation.</span>
<span id="L299">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L300">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L301">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L302">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L303">NK = 2                          !   [nondim]</span>
<span id="L304">                                ! The number of model layers.</span>
<span id="L305">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L306">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L307">                                ! production is set to 0.</span>
<span id="L308"></span>
<span id="L309">! === module MOM_tracer_registry ===</span>
<span id="L310"></span>
<span id="L311">! === module MOM_restart ===</span>
<span id="L312">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L313">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L314">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L315">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L316">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L317">                                ! The name-root of the restart file.</span>
<span id="L318">MAX_FIELDS = 50                 ! default = 100</span>
<span id="L319">                                ! The maximum number of restart fields that can be used.</span>
<span id="L320">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L321">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L322">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L323">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L324">                                ! checksums will not match and cause crash.</span>
<span id="L325">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L326">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L327">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L328">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L329">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L330">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L331">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L332">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L333">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L334">                                ! signals in the simulation.</span>
<span id="L335"></span>
<span id="L336">! === module MOM_tracer_flow_control ===</span>
<span id="L337">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L338">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L339">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L340">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L341">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L342">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L343">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L344">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L345">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L346">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L347">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L348">                                ! If true, use the MARBL tracer package.</span>
<span id="L349">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L350">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L351">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L352">                                ! If true, use the file dyes tracer package.</span>
<span id="L353">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L354">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L355">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L356">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L357">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L358">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L359">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L360">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L361">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L362">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L363">                                ! MOM_generic_tracer packages.</span>
<span id="L364">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L365">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L366">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L367">                                ! If true, use the boundary impulse tracer.</span>
<span id="L368">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L369">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L370">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L371">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L372"></span>
<span id="L373">! === module MOM_coord_initialization ===</span>
<span id="L374">COORD_CONFIG = &quot;gprime&quot;         ! default = &quot;none&quot;</span>
<span id="L375">                                ! This specifies how layers are to be defined:</span>
<span id="L376">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L377">                                !     file - read coordinate information from the file</span>
<span id="L378">                                !       specified by (COORD_FILE).</span>
<span id="L379">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L380">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L381">                                !     linear - linear based on interfaces not layers</span>
<span id="L382">                                !     layer_ref - linear based on layer densities</span>
<span id="L383">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L384">                                !     ts_range - use range of temperature and salinity</span>
<span id="L385">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L386">                                !       and GINT calculate internal densities.</span>
<span id="L387">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L388">                                !       density and GINT calculate internal densities.</span>
<span id="L389">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L390">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L391">                                !     USER - call a user modified routine.</span>
<span id="L392">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L393">                                ! The reduced gravity at the free surface.</span>
<span id="L394">GINT = 0.0196                   !   [m s-2]</span>
<span id="L395">                                ! The reduced gravity across internal interfaces.</span>
<span id="L396">LIGHTEST_DENSITY = 1031.0       !   [kg m-3] default = 1031.0</span>
<span id="L397">                                ! The reference potential density used for layer 1.</span>
<span id="L398"></span>
<span id="L399">! === module MOM_state_initialization ===</span>
<span id="L400">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L401">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L402">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L403">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L404">INIT_LAYERS_FROM_Z_FILE = False !   [Boolean] default = False</span>
<span id="L405">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L406">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L407">THICKNESS_CONFIG = &quot;phillips&quot;   ! default = &quot;uniform&quot;</span>
<span id="L408">                                ! A string that determines how the initial layer thicknesses are specified for a</span>
<span id="L409">                                ! new run:</span>
<span id="L410">                                !     file - read interface heights from the file specified</span>
<span id="L411">                                !       by (THICKNESS_FILE).</span>
<span id="L412">                                !     thickness_file - read thicknesses from the file specified</span>
<span id="L413">                                !       by (THICKNESS_FILE).</span>
<span id="L414">                                !     mass_file - read thicknesses in units of mass per unit area from the file</span>
<span id="L415">                                !       specified by (THICKNESS_FILE).</span>
<span id="L416">                                !     coord - determined by ALE coordinate.</span>
<span id="L417">                                !     uniform - uniform thickness layers evenly distributed</span>
<span id="L418">                                !       between the surface and MAXIMUM_DEPTH.</span>
<span id="L419">                                !     list - read a list of positive interface depths.</span>
<span id="L420">                                !     param - use thicknesses from parameter THICKNESS_INIT_VALUES.</span>
<span id="L421">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L422">                                !       DOME sill-overflow test case.</span>
<span id="L423">                                !     ISOMIP - use a configuration for the</span>
<span id="L424">                                !       ISOMIP test case.</span>
<span id="L425">                                !     benchmark - use the benchmark test case thicknesses.</span>
<span id="L426">                                !     Neverworld - use the Neverworld test case thicknesses.</span>
<span id="L427">                                !     search - search a density profile for the interface</span>
<span id="L428">                                !       densities. This is not yet implemented.</span>
<span id="L429">                                !     circle_obcs - the circle_obcs test case is used.</span>
<span id="L430">                                !     DOME2D - 2D version of DOME initialization.</span>
<span id="L431">                                !     adjustment2d - 2D lock exchange thickness ICs.</span>
<span id="L432">                                !     sloshing - sloshing gravity thickness ICs.</span>
<span id="L433">                                !     seamount - no motion test with seamount ICs.</span>
<span id="L434">                                !     dumbbell - sloshing channel ICs.</span>
<span id="L435">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L436">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L437">                                !     USER - call a user modified routine.</span>
<span id="L438">HALF_STRAT_DEPTH = 0.25         !   [nondim] default = 0.5</span>
<span id="L439">                                ! The fractional depth where the stratification is centered.</span>
<span id="L440">JET_WIDTH = 200.0               !   [km]</span>
<span id="L441">                                ! The width of the zonal-mean jet.</span>
<span id="L442">JET_HEIGHT = 300.0              !   [m]</span>
<span id="L443">                                ! The interface height scale associated with the zonal-mean jet.</span>
<span id="L444">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L445">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L446">                                ! surface pressure is applied.</span>
<span id="L447">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L448">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L449">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L450">                                ! read from file.</span>
<span id="L451">VELOCITY_CONFIG = &quot;phillips&quot;    ! default = &quot;zero&quot;</span>
<span id="L452">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L453">                                ! run:</span>
<span id="L454">                                !     file - read velocities from the file specified</span>
<span id="L455">                                !       by (VELOCITY_FILE).</span>
<span id="L456">                                !     zero - the fluid is initially at rest.</span>
<span id="L457">                                !     uniform - the flow is uniform (determined by</span>
<span id="L458">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L459">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L460">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L461">                                !     USER - call a user modified routine.</span>
<span id="L462">VELOCITY_IC_PERTURB_AMP = 0.001 !   [m s-1] default = 0.001</span>
<span id="L463">                                ! The magnitude of the initial velocity perturbation.</span>
<span id="L464">PHILLIPS_ANSWER_DATE = 20241201 ! default = 20241201</span>
<span id="L465">                                ! The vintage of the expressions in the Phillips_initialization code.  Values</span>
<span id="L466">                                ! below 20250101 recover the answers from the end of 2018, while higher values</span>
<span id="L467">                                ! use mathematically equivalent expressions that are fully rescalable.</span>
<span id="L468">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L469">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L470">SPONGE = True                   !   [Boolean] default = False</span>
<span id="L471">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L472">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L473">SPONGE_CONFIG = &quot;phillips&quot;      ! default = &quot;file&quot;</span>
<span id="L474">                                ! A string that sets how the sponges are configured:</span>
<span id="L475">                                !     file - read sponge properties from the file</span>
<span id="L476">                                !       specified by (SPONGE_FILE).</span>
<span id="L477">                                !     ISOMIP - apply ale sponge in the ISOMIP case</span>
<span id="L478">                                !     RGC - apply sponge in the rotating_gravity_current case</span>
<span id="L479">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L480">                                !       DOME sill-overflow test case.</span>
<span id="L481">                                !     BFB - Sponge at the southern boundary of the domain</span>
<span id="L482">                                !       for buoyancy-forced basin case.</span>
<span id="L483">                                !     USER - call a user modified routine.</span>
<span id="L484">SPONGE_RATE = 1.157407407407407E-06 !   [s-1] default = 1.157407407407407E-06</span>
<span id="L485">                                ! The rate at which the zonal-mean sponges damp.</span>
<span id="L486">!Total sponge columns = 0       !</span>
<span id="L487">                                ! The total number of columns where sponges are applied.</span>
<span id="L488"></span>
<span id="L489">! === module MOM_diag_mediator ===</span>
<span id="L490">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L491">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L492">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L493">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L494">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L495">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L496">                                ! false.</span>
<span id="L497">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L498">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L499">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L500">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L501">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L502">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L503">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L504">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L505">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L506">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L507">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L508">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L509">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L510">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L511">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L512">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L513">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L514">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L515">                                ! be included in a diag_table.</span>
<span id="L516">DIAG_COORD_DEF_Z = &quot;UNIFORM&quot;    ! default = &quot;UNIFORM&quot;</span>
<span id="L517">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L518">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L519">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L520">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L521">                                !                the filename and variable name, separated</span>
<span id="L522">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L523">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L524">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L525">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L526">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L527">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L528">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L529">                                !                the filename and two variable names, separated</span>
<span id="L530">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L531">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L532">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L533">                                !                the filename and two 3D variable names, separated</span>
<span id="L534">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L535">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L536">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L537">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L538">                                !                the filename and three variable names, separated</span>
<span id="L539">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L540">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L541">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L542">                                !                Map typically contains integer values, but it can</span>
<span id="L543">                                !                contain real values, I+w, which imply using</span>
<span id="L544">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L545">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L546">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L547"></span>
<span id="L548">! === module MOM_MEKE ===</span>
<span id="L549">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L550">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L551">                                ! kinetic energy budget.</span>
<span id="L552"></span>
<span id="L553">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L554">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L555">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L556">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L557">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L558">                                ! file.</span>
<span id="L559">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L560">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L561">                                ! thickness diffusivity.</span>
<span id="L562">RESOLN_SCALED_KH = True         !   [Boolean] default = False</span>
<span id="L563">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L564">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L565">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L566">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L567">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L568">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L569">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L570">RESOLN_SCALED_KHTH = True       !   [Boolean] default = False</span>
<span id="L571">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L572">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L573">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L574">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L575">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L576">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L577">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L578">                                ! wave for calculating the resolution fn.</span>
<span id="L579">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L580">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L581">                                ! structure.</span>
<span id="L582">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L583">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L584">                                ! that BS_EBT_power=0</span>
<span id="L585">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L586">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L587">                                ! thickness diffusivity.</span>
<span id="L588">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L589">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L590">                                ! of thickness diffusivity.</span>
<span id="L591">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L592">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L593">                                ! tracer diffusivity.</span>
<span id="L594">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L595">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L596">                                ! of tracer diffusivity.</span>
<span id="L597">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L598">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L599">                                ! diffusivity in the GL90 scheme.</span>
<span id="L600">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L601">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L602">                                ! diffusivity in the GL90 scheme.</span>
<span id="L603">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L604">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L605">                                ! diffusivity</span>
<span id="L606">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L607">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L608">                                ! diffusivity</span>
<span id="L609">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L610">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L611">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L612">                                ! should be necessary.</span>
<span id="L613">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L614">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L615">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L616">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L617">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L618">                                ! code.</span>
<span id="L619">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L620">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L621">                                ! &amp; S into thin layers.</span>
<span id="L622">KH_RES_SCALE_COEF = 0.707106781 !   [nondim] default = 1.0</span>
<span id="L623">                                ! A coefficient that determines how KhTh is scaled away if RESOLN_SCALED_... is</span>
<span id="L624">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER).</span>
<span id="L625">KH_RES_FN_POWER = 100           ! default = 2</span>
<span id="L626">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L627">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L628">                                ! greater than 100 results in a step-function being used.</span>
<span id="L629">VISC_RES_SCALE_COEF = 0.707106781 !   [nondim] default = 0.707106781</span>
<span id="L630">                                ! A coefficient that determines how Kh is scaled away if RESOLN_SCALED_... is</span>
<span id="L631">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER). This</span>
<span id="L632">                                ! function affects lateral viscosity, Kh, and not KhTh.</span>
<span id="L633">VISC_RES_FN_POWER = 100         ! default = 100</span>
<span id="L634">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L635">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L636">                                ! greater than 100 results in a step-function being used. This function affects</span>
<span id="L637">                                ! lateral viscosity, Kh, and not KhTh.</span>
<span id="L638">INTERPOLATE_RES_FN = False      !   [Boolean] default = False</span>
<span id="L639">                                ! If true, interpolate the resolution function to the velocity points from the</span>
<span id="L640">                                ! thickness points; otherwise interpolate the wave speed and calculate the</span>
<span id="L641">                                ! resolution function independently at each point.</span>
<span id="L642">GILL_EQUATORIAL_LD = True       !   [Boolean] default = True</span>
<span id="L643">                                ! If true, uses Gill&#x27;s definition of the baroclinic equatorial deformation</span>
<span id="L644">                                ! radius, otherwise, if false, use Pedlosky&#x27;s definition. These definitions</span>
<span id="L645">                                ! differ by a factor of 2 in front of the beta term in the denominator. Gill&#x27;s</span>
<span id="L646">                                ! is the more appropriate definition.</span>
<span id="L647">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L648">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L649">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L650">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L651">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L652">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L653">                                ! starting point for iterations.</span>
<span id="L654">EBT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L655">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L656">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L657">                                ! this option to false.</span>
<span id="L658">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L659">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L660"></span>
<span id="L661">! === module MOM_set_visc ===</span>
<span id="L662">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L663">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L664">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L665">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L666">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L667">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L668">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L669">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L670">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L671">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L672">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L673">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L674">                                ! layer is HBBL.</span>
<span id="L675">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L676">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L677">                                ! fraction of the bottom it overlies.</span>
<span id="L678">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L679">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L680">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L681">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L682">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L683">                                ! thickness for viscosity.</span>
<span id="L684">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L685">                                ! The rotation rate of the earth.</span>
<span id="L686">HBBL = 10.0                     !   [m]</span>
<span id="L687">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L688">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L689">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L690">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L691">CDRAG = 0.01                    !   [nondim] default = 0.003</span>
<span id="L692">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L693">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L694">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L695">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L696">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L697">                                ! and LINEAR_DRAG is false.</span>
<span id="L698">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L699">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L700">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L701">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L702">                                ! defined.</span>
<span id="L703">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L704">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L705">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L706">                                ! near-bottom viscosity.</span>
<span id="L707">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L708">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L709">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L710">                                ! viscosity.</span>
<span id="L711">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L712">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L713">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L714">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L715">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L716">                                ! m2 s-1, may be used.</span>
<span id="L717">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L718">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L719">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L720">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L721">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L722">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L723">                                ! the bottom layer feels the intended drag.</span>
<span id="L724"></span>
<span id="L725">! === module MOM_thickness_diffuse ===</span>
<span id="L726">KHTH = 8000.0                   !   [m2 s-1] default = 0.0</span>
<span id="L727">                                ! The background horizontal thickness diffusivity.</span>
<span id="L728">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L729">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L730">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L731">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L732">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L733">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L734">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L735">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L736">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L737">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L738">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L739">                                ! models.</span>
<span id="L740">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L741">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L742">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L743">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L744">                                ! are scaled back proportionately.</span>
<span id="L745">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L746">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L747">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L748">                                ! the layer density structure).</span>
<span id="L749">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L750">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L751">                                ! horizontally smooth jagged layers.</span>
<span id="L752">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L753">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L754">                                ! scaled away.</span>
<span id="L755">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L756">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L757">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L758">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L759">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L760">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L761">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L762">                                ! streamfunction for the GM source term.</span>
<span id="L763">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L764">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L765">                                ! (Marshall et al., 2012).</span>
<span id="L766">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L767">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L768">                                ! McWilliams parameterization.</span>
<span id="L769">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L770">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L771">                                ! sign, for legacy reproducibility.</span>
<span id="L772"></span>
<span id="L773">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L774">TIDES = False                   !   [Boolean] default = False</span>
<span id="L775">                                ! If true, apply tidal momentum forcing.</span>
<span id="L776">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L777">                                ! If true, calculate self-attraction and loading.</span>
<span id="L778">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L779">                                ! If true, perform inline harmonic analysis.</span>
<span id="L780">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L781">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L782">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L783">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L784">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L785">                                ! and USE_RK2 is true.</span>
<span id="L786">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L787">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L788">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L789">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L790">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L791">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L792">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L793">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L794">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L795">                                ! barotropic solver.</span>
<span id="L796">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L797">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L798">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L799">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L800">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L801">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L802">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L803">                                ! step.</span>
<span id="L804">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L805">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L806">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L807">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L808">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L809">                                ! gradient.</span>
<span id="L810">VISC_REM_BUG = True             !   [Boolean] default = False</span>
<span id="L811">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L812">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L813">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L814">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L815">VISC_REM_TIMESTEP_BUG = True    !   [Boolean] default = True</span>
<span id="L816">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L817">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L818">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L819"></span>
<span id="L820">! === module MOM_continuity_PPM ===</span>
<span id="L821">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L822">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L823">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L824">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L825">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L826">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L827">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L828">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L829">                                ! of accuracy of the dynamic core.</span>
<span id="L830">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L831">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L832">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L833">                                ! mode where its minimal stencil is useful.</span>
<span id="L834">ETA_TOLERANCE = 1.0E-10         !   [m] default = 1.0E-10</span>
<span id="L835">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L836">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L837">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L838">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L839">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L840">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L841">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L842">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L843">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L844">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L845">                                ! 0.5.</span>
<span id="L846">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L847">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L848">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L849">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L850">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L851">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L852">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L853">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L854">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L855">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L856">                                ! viscous columns.</span>
<span id="L857">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L858">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L859">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L860"></span>
<span id="L861">! === module MOM_CoriolisAdv ===</span>
<span id="L862">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L863">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L864">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L865">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L866">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L867">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L868">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L869">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L870">                                ! used.</span>
<span id="L871">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L872">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L873">                                ! values are:</span>
<span id="L874">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L875">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L876">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L877">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L878">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L879">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L880">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L881">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L882">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L883">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L884">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L885">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L886">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L887">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L888">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L889">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L890">                                ! energy gradient. Valid values are:</span>
<span id="L891">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L892">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L893">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L894">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L895">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L896"></span>
<span id="L897">! === module MOM_PressureForce ===</span>
<span id="L898">ANALYTIC_FV_PGF = False         !   [Boolean] default = True</span>
<span id="L899">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L900">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L901">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L902">                                ! al., O. Mod. (2008).</span>
<span id="L903"></span>
<span id="L904">! === module MOM_PressureForce_Mont ===</span>
<span id="L905"></span>
<span id="L906">! === module MOM_Zanna_Bolton ===</span>
<span id="L907">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L908">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L909">                                ! mesoscale eddies.</span>
<span id="L910"></span>
<span id="L911">! === module MOM_hor_visc ===</span>
<span id="L912">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L913">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L914">                                ! Leith)</span>
<span id="L915">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L916">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L917">                                ! currently only works with split mode.</span>
<span id="L918">LAPLACIAN = False               !   [Boolean] default = False</span>
<span id="L919">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L920">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L921">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L922">                                ! LAPLACIAN.</span>
<span id="L923">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L924">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L925">AH_VEL_SCALE = 0.003            !   [m s-1] default = 0.0</span>
<span id="L926">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L927">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L928">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L929">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L930">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L931">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L932">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L933">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L934">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L935">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L936">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L937">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L938">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L939">                                ! harmonic backscatter.</span>
<span id="L940">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L941">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L942">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L943">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L944">                                ! Reynolds number is equal to this.</span>
<span id="L945">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L946">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L947">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L948">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L949">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L950">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L951">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L952">                                ! false).</span>
<span id="L953">BOUND_CORIOLIS_VEL = 10.0       !   [m s-1] default = 10.0</span>
<span id="L954">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L955">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L956">                                ! by MAXVEL.</span>
<span id="L957">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L958">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L959">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L960">                                ! outside of the domain.</span>
<span id="L961">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L962">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L963">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L964">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L965">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L966">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L967">                                ! recommended.</span>
<span id="L968"></span>
<span id="L969">! === module MOM_vert_friction ===</span>
<span id="L970">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L971">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L972">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L973">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L974">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L975">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L976">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L977">DIRECT_STRESS = True            !   [Boolean] default = False</span>
<span id="L978">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L979">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L980">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L981">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L982">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L983">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L984">                                ! of the ocean in a column.</span>
<span id="L985">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L986">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L987">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L988">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L989">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L990">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L991">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L992">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L993">HARMONIC_VISC = True            !   [Boolean] default = False</span>
<span id="L994">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L995">                                ! viscosity.</span>
<span id="L996">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L997">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L998">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L999">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1000">HMIX_FIXED = 20.0               !   [m]</span>
<span id="L1001">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1002">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1003">HMIX_STRESS = 20.0              !   [m] default = 20.0</span>
<span id="L1004">                                ! The depth over which the wind stress is applied if DIRECT_STRESS is true.</span>
<span id="L1005">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1006">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1007">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1008">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1009">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1010">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1011">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1012">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1013">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1014">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1015">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1016">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1017">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1018">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1019">                                ! default is CFL_TRUNCATE.</span>
<span id="L1020">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1021">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1022">                                ! the run.</span>
<span id="L1023">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1024">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1025">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1026">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1027">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1028">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1029">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1030">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1031">                                ! divided by the age of the universe.</span>
<span id="L1032"></span>
<span id="L1033">! === module MOM_barotropic ===</span>
<span id="L1034">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1035">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1036">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1037">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1038">                                ! true.</span>
<span id="L1039">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1040">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1041">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1042">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1043">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1044">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1045">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1046">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1047">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1048">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1049">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1050">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1051">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1052">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1053">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1054">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1055">                                ! linearized.</span>
<span id="L1056">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1057">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1058">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1059">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1060">                                ! for truncation errors.</span>
<span id="L1061">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1062">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1063">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1064">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1065">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1066">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1067">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1068">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1069">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1070">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1071">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1072">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1073">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1074">DYNAMIC_SURFACE_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1075">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1076">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1077">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1078">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1079">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1080">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1081">                                ! efficient or general expressions.</span>
<span id="L1082">VISC_REM_BT_WEIGHT_BUG = True   !   [Boolean] default = True</span>
<span id="L1083">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1084">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1085">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1086">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1087">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1088">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1089">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1090">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1091">                                ! set to True for new experiments</span>
<span id="L1092">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1093">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1094">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1095">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1096">                                ! probably be used.</span>
<span id="L1097">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1098">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1099">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1100">                                ! values are:</span>
<span id="L1101">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1102">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1103">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1104">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1105">                                !       mean for layers below, and a weighted average for</span>
<span id="L1106">                                !       layers that straddle that depth</span>
<span id="L1107">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1108">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1109">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1110">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1111">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1112">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1113">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1114">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1115">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1116">                                ! facilitate tide modeling.</span>
<span id="L1117">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1118">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1119">                                ! band-pass filter must be turned on.</span>
<span id="L1120">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1121">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1122">                                ! only be used as a desperate debugging measure.</span>
<span id="L1123">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1124">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1125">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1126">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1127">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1128">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1129">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1130">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1131">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1132">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1133">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1134">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1135">                                ! MAXIMUM_DEPTH.</span>
<span id="L1136">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1137">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1138">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1139">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1140">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1141">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1142">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1143">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1144">                                ! 0.05.</span>
<span id="L1145">DTBT = -0.9                     !   [s or nondim] default = -0.98</span>
<span id="L1146">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1147">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1148">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1149">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1150">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1151">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1152">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1153">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1154">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1155">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1156">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1157">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1158">                                ! not alter the solutions themselves.</span>
<span id="L1159"></span>
<span id="L1160">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1161">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L1162">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1163">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1164">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1165"></span>
<span id="L1166">! === module MOM_diagnostics ===</span>
<span id="L1167">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1168">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1169">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1170">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1171">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1172">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1173">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1174">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1175">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1176">                                ! this option to false.</span>
<span id="L1177"></span>
<span id="L1178">! === module MOM_diabatic_driver ===</span>
<span id="L1179">! The following parameters are used for diabatic processes.</span>
<span id="L1180">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1181">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1182">                                ! and is needed to avoid change in answers.</span>
<span id="L1183">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1184">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1185">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1186">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1187">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1188">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1189">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1190">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1191">                                ! internal tide energy density.</span>
<span id="L1192">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1193">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1194">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1195">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1196">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1197">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1198">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1199">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1200">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1201">                                ! updated state.</span>
<span id="L1202">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1203">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1204">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1205">KD_MIN_TR = 1.0E-05             !   [m2 s-1] default = 1.0E-05</span>
<span id="L1206">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1207">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1208">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1209">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1210">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1211">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1212">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1213">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1214">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1215">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1216">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1217">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1218">                                ! scale.</span>
<span id="L1219">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1220">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1221">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1222">                                ! through the column.</span>
<span id="L1223">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1224">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1225">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1226">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1227">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1228">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1229">                                ! base of the mixed layer.</span>
<span id="L1230"></span>
<span id="L1231">! === module MOM_CVMix_KPP ===</span>
<span id="L1232">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1233">! See http://cvmix.github.io/</span>
<span id="L1234">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1235">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1236">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1237"></span>
<span id="L1238">! === module MOM_CVMix_conv ===</span>
<span id="L1239">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1240">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1241">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1242">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1243">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1244"></span>
<span id="L1245">! === module MOM_entrain_diffusive ===</span>
<span id="L1246">MAX_ENT_IT = 20                 ! default = 5</span>
<span id="L1247">                                ! The maximum number of iterations that may be used to calculate the interior</span>
<span id="L1248">                                ! diapycnal entrainment.</span>
<span id="L1249">TOLERANCE_ENT = 1.0E-05         !   [m] default = 2.449489742783178E-05</span>
<span id="L1250">                                ! The tolerance with which to solve for entrainment values.</span>
<span id="L1251"></span>
<span id="L1252">! === module MOM_set_diffusivity ===</span>
<span id="L1253">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1254">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1255">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1256">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1257">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1258">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1259">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1260">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1261">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1262">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1263"></span>
<span id="L1264">! === module MOM_tidal_mixing ===</span>
<span id="L1265">! Vertical Tidal Mixing Parameterization</span>
<span id="L1266">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1267">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1268">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1269">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1270">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1271">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L1272">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1273">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1274">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1275">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1276">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1277">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1278">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1279">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1280">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1281">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1282">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1283">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1284">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1285">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1286">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1287">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1288">                                ! scheme.</span>
<span id="L1289">DRAG_DIFFUSIVITY_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1290">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1291">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1292">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1293">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1294">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1295">                                ! boundary layer density.</span>
<span id="L1296">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1297">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1298">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1299">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1300"></span>
<span id="L1301">! === module MOM_bkgnd_mixing ===</span>
<span id="L1302">! Adding static vertical background mixing coefficients</span>
<span id="L1303">KD = 1.0E-04                    !   [m2 s-1] default = 0.0</span>
<span id="L1304">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1305">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1306">KD_MIN = 1.0E-06                !   [m2 s-1] default = 1.0E-06</span>
<span id="L1307">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1308">KD_ML_TOT = 1.0E-04             !   [m2 s-1] default = 1.0E-04</span>
<span id="L1309">                                ! The total diapcynal diffusivity in the surface mixed layer when there is not a</span>
<span id="L1310">                                ! physically based parameterization of mixing in the mixed layer, such as bulk</span>
<span id="L1311">                                ! mixed layer or KPP or ePBL.</span>
<span id="L1312">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1313">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1314">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1315">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1316">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1317">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1318">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1319">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1320">                                ! into viscosities.</span>
<span id="L1321">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1322">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1323">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1324">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1325">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1326">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1327">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1328">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1329">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1330">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1331">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1332">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1333">                                ! or scaling.</span>
<span id="L1334">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1335">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1336">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1337">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1338">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1339">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1340">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1341">                                ! = A + B*N.</span>
<span id="L1342">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1343">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1344">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1345">                                ! = A + B*N</span>
<span id="L1346">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1347">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1348">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1349">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1350">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1351"></span>
<span id="L1352">! === module MOM_kappa_shear ===</span>
<span id="L1353">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1354">USE_JACKSON_PARAM = False       !   [Boolean] default = False</span>
<span id="L1355">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1356">                                ! parameterization.</span>
<span id="L1357">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1358">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1359">                                ! tracer points in the kappa shear solver.</span>
<span id="L1360">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1361">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1362">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1363">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1364">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1365">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1366">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1367">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1368">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1369">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1370">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1371"></span>
<span id="L1372">! === module MOM_CVMix_shear ===</span>
<span id="L1373">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1374">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1375">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1376">                                ! parameterization.</span>
<span id="L1377">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1378">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1379">                                ! parameterization.</span>
<span id="L1380"></span>
<span id="L1381">! === module MOM_CVMix_ddiff ===</span>
<span id="L1382">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1383">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1384">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1385">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1386">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1387"></span>
<span id="L1388">! === module MOM_diabatic_aux ===</span>
<span id="L1389">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1390">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1391">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1392"></span>
<span id="L1393">! === module MOM_regularize_layers ===</span>
<span id="L1394">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L1395">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L1396">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L1397"></span>
<span id="L1398">! === module MOM_tracer_advect ===</span>
<span id="L1399">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L1400">                                ! The horizontal transport scheme for tracers:</span>
<span id="L1401">                                !   PLM    - Piecewise Linear Method</span>
<span id="L1402">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L1403">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L1404"></span>
<span id="L1405">! === module MOM_tracer_hor_diff ===</span>
<span id="L1406">KHTR = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L1407">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L1408">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1409">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L1410">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1411">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L1412">                                ! activate.</span>
<span id="L1413">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L1414">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L1415">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L1416">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L1417">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L1418">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L1419">                                ! tracers to thickness mixing.</span>
<span id="L1420">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L1421">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L1422">                                ! interior.</span>
<span id="L1423">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L1424">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L1425">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L1426">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L1427">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L1428">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L1429">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L1430">                                ! iterations is often this value or the next greater integer.</span>
<span id="L1431">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L1432">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L1433">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L1434">                                ! positions of the surfaces do not change</span>
<span id="L1435"></span>
<span id="L1436">! === module MOM_neutral_diffusion ===</span>
<span id="L1437">! This module implements neutral diffusion of tracers</span>
<span id="L1438">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L1439">                                ! If true, enables the neutral diffusion module.</span>
<span id="L1440"></span>
<span id="L1441">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1442">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1443">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1444">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1445">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1446">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1447">                                ! error rather than issue a WARNING.</span>
<span id="L1448"></span>
<span id="L1449">! === module MOM_sum_output ===</span>
<span id="L1450">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1451">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1452">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1453">                                ! dramatically.</span>
<span id="L1454">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1455">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1456">                                ! are written.</span>
<span id="L1457">MAXTRUNC = 0                    !   [truncations save_interval-1] default = 0</span>
<span id="L1458">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1459">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1460">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1461">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1462">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1463">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1464">                                ! 10*MAXVEL^2.</span>
<span id="L1465">MAXVEL = 10.0                   !   [m s-1] default = 3.0E+08</span>
<span id="L1466">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1467">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1468">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1469">DATE_STAMPED_STDOUT = False     !   [Boolean] default = True</span>
<span id="L1470">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1471">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1472">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1473">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L1474">                                ! The time unit in seconds a number of input fields</span>
<span id="L1475">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1476">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1477">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1478">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1479">                                ! file.</span>
<span id="L1480">ENERGYSAVEDAYS = 1.0            !   [days] default = 1.0</span>
<span id="L1481">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1482">                                ! other globally summed diagnostics.</span>
<span id="L1483">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L1484">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1485">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1486">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1487"></span>
<span id="L1488">! === module ocean_stochastics_init ===</span>
<span id="L1489">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1490">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1491">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1492">                                ! UFS model only.</span>
<span id="L1493">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1494">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1495">                                ! energy backscatter scheme.</span>
<span id="L1496">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1497">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1498">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1499">                                ! namelist in the UFS model only.</span>
<span id="L1500"></span>
<span id="L1501">! === module MOM_surface_forcing ===</span>
<span id="L1502">VARIABLE_WINDS = False          !   [Boolean] default = True</span>
<span id="L1503">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1504">VARIABLE_BUOYFORCE = False      !   [Boolean] default = True</span>
<span id="L1505">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1506">                                ! model.</span>
<span id="L1507">BUOY_CONFIG = &quot;zero&quot;            ! default = &quot;zero&quot;</span>
<span id="L1508">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1509">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1510">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1511">WIND_CONFIG = &quot;zero&quot;            ! default = &quot;zero&quot;</span>
<span id="L1512">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1513">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1514">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1515">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L1516">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1517">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1518">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1519">                                ! The latent heat of fusion.</span>
<span id="L1520">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1521">                                ! The latent heat of fusion.</span>
<span id="L1522">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1523">                                ! The background gustiness in the winds.</span>
<span id="L1524">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L1525">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L1526">                                ! velocity</span>
<span id="L1527">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L1528">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L1529"></span>
<span id="L1530">! === module MOM_restart ===</span>
<span id="L1531">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L1532">                                ! If true, enables surface wave modules.</span>
<span id="L1533"></span>
<span id="L1534">! === module MOM_main (MOM_driver) ===</span>
<span id="L1535">DT_FORCING = 3600.0             !   [s] default = 600.0</span>
<span id="L1536">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L1537">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L1538">DAYMAX = 20.0                   !   [days]</span>
<span id="L1539">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L1540">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L1541">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L1542">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L1543">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L1544">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L1545">RESTART_CONTROL = 3             ! default = 1</span>
<span id="L1546">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L1547">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L1548">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L1549">                                ! non-negative value.</span>
<span id="L1550">RESTINT = 730.0                 !   [days] default = 0.0</span>
<span id="L1551">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L1552">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L1553">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L1554">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L1555">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L1556">                                ! an elapsed CPU time.</span>
<span id="L1557"></span>
<span id="L1558">! === module MOM_write_cputime ===</span>
<span id="L1559">MAXCPU = -1.0                   !   [wall-clock seconds] default = -1.0</span>
<span id="L1560">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L1561">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L1562">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L1563">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L1564">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L1565">                                ! processors used.</span>
<span id="L1566">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L1567">                                ! The file into which CPU time is written.</span>
<span id="L1568"></span>
<span id="L1569">! === module MOM_file_parser ===</span>
<span id="L1570">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L1571">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L1572">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L1573">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L1574">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L1575">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L1576">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L1577">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L1578">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L1579">                                ! MOM_parameter_doc.short .</span>
</pre>
